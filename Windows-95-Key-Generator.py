#-- coding: utf-8 --
import random

def generate_serial():
    # ����ǰ3λ����Χ001��366
    # Generate the first 3 digits, ranging from 001 to 366
    first_three = str(random.randint(1, 366)).zfill(3)

    # ���ɺ�2λ����Χ95��03��ʵ����Ӧ����95��99��00��03��
    # The last 2 digits generated range from 95 to 03 (actually it should be 95 to 99 and 00 to 03)
    year_suffix = str(random.randint(95, 99)).zfill(2)

    # ����3����ĸ��ֻ����OEM
    # Generate 3 letters, only OEM
    letters = 'OEM'

    # ����7�����֣���һλΪ0��������Ӻ�������7
    # Generate 7 numbers, the first digit is 0, and the rest can be divisible by 7 after adding them together
    first_digit = 0
    remaining_digits = [random.randint(0, 9) for _ in range(5)]  # 5��������� # 5 random numbers
    sum_of_digits = first_digit + sum(remaining_digits)
    last_digit = (7 - (sum_of_digits % 7)) % 7
    seven_digits = [first_digit] + remaining_digits + [last_digit]
    seven_digits_str = ''.join(map(str, seven_digits))
    # ����5λ�������
    # Generate 5 digit random numbers
    random_numbers = ''.join([str(random.randint(0, 9)) for _ in range(5)])

    # ƴ�ӳ����кŸ�ʽ��ʹ�ö̻��߷ָ�
    # Splice into serial number format, separated by dashes
    serial_number = f"{first_three}{year_suffix}-{letters}-{seven_digits_str}-{random_numbers}"
    
    return serial_number

# Generate serial number
# �������к�
serial = generate_serial()
print("Windows 95 key:", serial)
