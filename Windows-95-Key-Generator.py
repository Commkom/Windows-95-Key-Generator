#-- coding: utf-8 --
import random

def generate_serial():
    
    # 生成前 3 位数字，范围从 001 到 366
    # Generate the first 3 digits, ranging from 001 to 366
    first_three = str(random.randint(1, 366)).zfill(3)

    # 生成的最后 2 位数字范围从 95 到 03（实际上应该是 95 到 99 和 00 到 03）
    # The last 2 digits generated range from 95 to 03 (actually it should be 95 to 99 and 00 to 03)
    year_suffix = str(random.randint(95, 99)).zfill(2)

    # 生成7个数字，第一个数字是0，其余数字相加后可以被7整除
    # Generate 7 numbers, the first digit is 0, and the rest can be divisible by 7 after adding them together
    first_digit = 0
    remaining_digits = [random.randint(0, 9) for _ in range(5)]  
    sum_of_digits = first_digit + sum(remaining_digits)
    last_digit = (7 - (sum_of_digits % 7)) % 7
    seven_digits = [first_digit] + remaining_digits + [last_digit]
    seven_digits_str = ''.join(map(str, seven_digits))

    # 生成 5 位随机数
    # Generate 5 digit random numbers
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(5)])

    # 拼接成序列号格式，用破折号分隔
    # Splice into serial number format, separated by dashes
    serial_number = f"{first_three}{year_suffix}-OEM-{seven_digits_str}-{random_numbers}"
    
    return serial_number

# 生成序列号
# Generate serial number
serial = generate_serial()
print("Windows 95 key:", serial)
input("Press Enter to exit...")
