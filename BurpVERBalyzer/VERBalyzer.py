# VERBalyzer - Burp Plugin to detect HTTP Methods supported by the server
# Author: Ray Doyle (@doylersec) <https://www.doyler.net>
# Copyright 2017
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from burp import IBurpExtender
    from burp import IScannerCheck
    from burp import IScanIssue
    from burp import IScannerInsertionPointProvider
    from burp import IScannerInsertionPoint
    from burp import IParameter
    from array import array
    from org.python.core.util import StringUtil
    import string
except ImportError:
    print("Failed to load dependencies.")

VERSION = "1.0"
callbacks = None
helpers = None

methods = [
    'OPTIONS',
    #'GET',
    #'HEAD',
    #'POST',
    'PUT',
    #'DELETE',
    'TRACE',
    'CONNECT'
    'PROPFIND',
    'PROPPATCH',
    'MKCOL',
    'COPY',
    'MOVE',
    'LOCK',
    'UNLOCK',
    'VERSION-CONTROL',
    'REPORT',
    'CHECKOUT',
    'CHECKIN',
    'UNCHECKOUT',
    'MKWORKSPACE',
    'UPDATE',
    'LABEL',
    'MERGE',
    'BASELINE-CONTROL',
    'MKACTIVITY',
    'ORDERPATCH',
    'ACL',
    'SEARCH',
    'PATCH',
    'FOO'
]

class BurpExtender(IBurpExtender, IScannerInsertionPointProvider, IScannerCheck):
    def	registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.setExtensionName("VERBalyzer")

        callbacks.registerScannerInsertionPointProvider(self)
        callbacks.registerScannerCheck(self)

        print("Successfully loaded VERBalyzer v" + VERSION)
        return

    # helper method to search a response for occurrences of a literal match string
    # and return a list of start/end offsets
    def _get_matches(self, response, match):
        matches = []
        start = 0
        reslen = len(response)
        matchlen = len(match)
        while start < reslen:
            start = self._helpers.indexOf(response, match, True, start, reslen)
            if start == -1:
                break
            matches.append(array('i', [start, start + matchlen]))
            start += matchlen

        return matches

    # 
    # implement IScannerInsertionPointProvider
    #
    def getInsertionPoints(self, baseRequestResponse):
        requestLine = self._helpers.analyzeRequest(baseRequestResponse.getRequest()).getHeaders()[0]

        if (requestLine is None):
            return None
        
        else:
            # if the parameter is present, add a single custom insertion point for it
            return [ InsertionPoint(self._helpers, baseRequestResponse.getRequest(), requestLine) ]
        
    def doActiveScan(self, baseRequestResponse, insertionPoint):
        if 'HTTP Method' != insertionPoint.getInsertionPointName():
            return []

        issues = []
        
        for method in methods:
            checkRequest = insertionPoint.buildRequest(method)
            checkRequestResponse = self._callbacks.makeHttpRequest(baseRequestResponse.getHttpService(), checkRequest)

            matches = self._get_matches(checkRequestResponse.getResponse(), "HTTP/1.1 200 OK")

            if len(matches) > 0:
                # get the offsets of the payload within the request, for in-UI highlighting
                requestHighlights = [insertionPoint.getPayloadOffsets(method)]

                issues.append(CustomScanIssue(
                    baseRequestResponse.getHttpService(),
                    self._helpers.analyzeRequest(baseRequestResponse).getUrl(),
                    [self._callbacks.applyMarkers(checkRequestResponse, requestHighlights, matches)],
                    "Non-standard HTTP Method Found",
                    "The following method was found to be supported by the server: " + method,
                    "Medium"))

        return issues

    def doPassiveScan(self, basePair):
        return []

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        # This method is called when multiple issues are reported for the same URL 
        # path by the same extension-provided check. The value we return from this 
        # method determines how/whether Burp consolidates the multiple issues
        # to prevent duplication
        #
        # Since the issue name is sufficient to identify our issues as different,
        # if both issues have the same name, only report the existing issue
        # otherwise report both issues
        if existingIssue.getIssueDetail() == newIssue.getIssueDetail():
            return -1
        return 0

# 
# class implementing IScannerInsertionPoint
#

class InsertionPoint(IScannerInsertionPoint):

    def __init__(self, helpers, baseRequest, requestLine):
        self._helpers = helpers
        self._baseRequest = baseRequest

        # parse the location of the input string within the decoded data
        start = 0
        self._insertionPointPrefix = requestLine[:start]
        end = string.find(requestLine, " /", start)
        if (end == -1):
            end = requestLine.length()
        self._baseValue = requestLine[start:end]
        self._insertionPointSuffix = requestLine[end:]
        return
        
    # 
    # implement IScannerInsertionPoint
    #
    def getInsertionPointName(self):
        return "HTTP Method"

    def getBaseValue(self):
        return self._baseValue

    def buildRequest(self, payload):
        # Gross workaround via Dafydd - https://support.portswigger.net/customer/portal/questions/12431820-design-of-active-scanner-plugin-vs-insertionpoints
        if payload.tostring() not in methods:
            raise Exception('Just stopping Burp from using our custom insertion point')
        else:
            requestStr = self._baseRequest.tostring()

            newRequest = requestStr.replace(self._baseValue, payload)
            newRequestB = StringUtil.toBytes(newRequest)
        
            # update the request with the new parameter value
            return newRequestB

    def getPayloadOffsets(self, payload):
        return [0, len(payload.tostring())]

    def getInsertionPointType(self):
        return INS_EXTENSION_PROVIDED

#
# class implementing IScanIssue to hold our custom scan issue details
#
class CustomScanIssue (IScanIssue):
    def __init__(self, httpService, url, httpMessages, name, detail, severity):
        self._httpService = httpService
        self._url = url
        self._httpMessages = httpMessages
        self._name = name
        self._detail = detail
        self._severity = severity

    def getUrl(self):
        return self._url

    def getIssueName(self):
        return self._name

    def getIssueType(self):
        return 0

    def getSeverity(self):
        return self._severity

    def getConfidence(self):
        return "Certain"

    def getIssueBackground(self):
        pass

    def getRemediationBackground(self):
        pass

    def getIssueDetail(self):
        return self._detail

    def getRemediationDetail(self):
        pass

    def getHttpMessages(self):
        return self._httpMessages

    def getHttpService(self):
        return self._httpService
