import gpiod
import time

# Chọn GPIO chip
chip = gpiod.Chip("/dev/gpiochip0")
line = chip.get_line(17)  # Chọn GPIO17 (chân 11)

# Cấu hình GPIO17 làm output
config = gpiod.LineSettings()
config.direction = gpiod.LineDirection.OUTPUT
line.request(config)

# Bật relay
print("Bật relay")
line.set_value(1)
time.sleep(5)

# Tắt relay
print("Tắt relay")
line.set_value(0)
