#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char *generate_serial() {
    // 生成前3位，范围001到366
    // Generate the first 3 digits, ranging from 001 to 366
    int first_three = (rand() % 366) + 1;

    // 生成后2位，范围95到03（实际上应该是95到99和00到03）
    // The last 2 digits generated range from 95 to 03 (actually it should be 95 to 99 and 00 to 03)
    int year_suffix = (rand() % 5) + 95;

    // 生成3个字母，只能是OEM
    // Generate 3 letters, only OEM
    char letters[] = "OEM";

    // 生成7个数字，第一位为0，其余相加后能整除7
    // Generate 7 numbers, the first digit is 0, and the rest can be divisible by 7 after adding them together
    int seven_digits[7];
    seven_digits[0] = 0;
    int sum_of_digits = 0;
    for (int i = 1; i < 6; i++) {
        seven_digits[i] = rand() % 10;
        sum_of_digits += seven_digits[i];
    }
    seven_digits[6] = (7 - (sum_of_digits % 7)) % 7;

    // 生成5位随机数字
    // Generate 5 digit random numbers
    int random_numbers = rand() % 100000;

    // 拼接成序列号格式，使用短划线分隔
    // Splice into serial number format, separated by dashes
    char *serial_number = (char *)malloc(sizeof(char) * 32);
    sprintf(serial_number, "%03d%02d-%s-%07d-%05d", first_three, year_suffix, letters, seven_digits[0] * 1000000 + seven_digits[1] * 100000 + seven_digits[2] * 10000 + seven_digits[3] * 1000 + seven_digits[4] * 100 + seven_digits[5] * 10 + seven_digits[6], random_numbers);
    return serial_number;
}

int main() {
    srand(time(NULL));
    char *serial = generate_serial();
    printf("Windows 95 key: %s\n", serial);
    printf("Press any key to close");
    free(serial);
    getchar();
}
