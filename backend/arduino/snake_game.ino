#include <LedControl.h>

// 初始化LED矩阵
LedControl lc = LedControl(12, 11, 10, 1);

// 摇杆引脚
const int xPin = A0;
const int yPin = A1;

void setup() {
  lc.shutdown(0, false);
  lc.setIntensity(0, 8);
  lc.clearDisplay(0);

  Serial.begin(9600);
}

void loop() {
  // 读取摇杆输入
  int xValue = analogRead(xPin);
  int yValue = analogRead(yPin);

  // 发送摇杆输入到Python
  Serial.print(xValue);
  Serial.print(",");
  Serial.println(yValue);

  // 处理来自Python的指令
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    // 解析并执行指令
    // 例如：command = "snake_pos:1,2;food_pos:3,4"
    // 更新LED矩阵显示
  }

  delay(100);
}