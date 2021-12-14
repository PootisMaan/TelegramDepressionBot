class CalculationSystem:

    def __init__(self, start_value=0):
        self.value = start_value

    def add_3(self):
        self.value += 3

    def add_2(self):
        self.value += 2

    def add_1(self):
        self.value += 1

    def add(self, num):
        self.value += num

    def get_value(self) -> int:
        return self.value

    def set_to_zero(self):
        self.value = 0

    def get_result(self) -> str:
        if self.value >= 31:
            return "Вероятность наличия у Вас депрессии крайне велика! Незамедлительно обратитесь к врачу-неврологу."
        elif 27 <= self.value <= 30:
            return "Да, у Вас, скорее всего, депрессия. Рекомендуем не откладывать визит к врачу-неврологу."
        elif 18 <= self.value <= 26:
            return "Возможно у Вас депрессия. Рекомендуем обратитесь к врачу-неврологу."
        elif 0 <= self.value <= 17:
            return "Поздравляем! У Вас нет признаков депрессии."
