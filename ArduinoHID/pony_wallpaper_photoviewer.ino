#include "Keyboard.h"

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

  // Wait 500ms
  delay(500);

  delay(5000);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_LEFT_ESC);
  Keyboard.releaseAll();

  delay(100);

  Keyboard.print("iexplore http://cdn32.sptndigital.com/sites/uk.tinypop/files/styles/image_1170x658/public/ct_series_f_primary_image/mylittlepony_show.jpg");

  typeKey(KEY_RETURN);

  delay(5000);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press('s');
  Keyboard.releaseAll();

  delay(2000);

  typeKey(KEY_RETURN);

  delay(300);

  Keyboard.press(KEY_LEFT_CTRL);
  Keyboard.press(KEY_LEFT_ESC);
  Keyboard.releaseAll();

  delay(300);

  Keyboard.print("%USERPROFILE%\\Documents\\mylittlepony_show.jpg");

  delay(500);

  typeKey(KEY_RETURN);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_TAB);

  delay(500);

  typeKey(KEY_RETURN);

  delay(500);

  typeKey(KEY_DOWN_ARROW);

  delay(500);

  typeKey(KEY_DOWN_ARROW);

  delay(500);

  typeKey(KEY_DOWN_ARROW);

  delay(500);

  typeKey(KEY_DOWN_ARROW);

  delay(500);

  typeKey(KEY_RETURN);

  delay(500);

  typeKey(KEY_DOWN_ARROW);

  delay(500);

  typeKey(KEY_DOWN_ARROW);

  delay(500);

  typeKey(KEY_RETURN);

  delay(500);

  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}