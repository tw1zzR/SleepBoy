
def number_to_words_uk(n: int, gender: str = "m", case: str = "nom") -> str:
    units_m = ["нуль", "один", "два", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
    units_f_nom = ["нуль", "одна", "дві", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]
    units_f_acc = ["нуль", "одну", "дві", "три", "чотири", "п’ять", "шість", "сім", "вісім", "дев’ять"]

    teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять",
             "п’ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев’ятнадцять"]
    tens = ["", "", "двадцять", "тридцять", "сорок", "п’ятдесят", "шістдесят"]

    if gender == "f":
        if case == "acc":
            units = units_f_acc
        else:
            units = units_f_nom
    else:
        units = units_m

    if n < 10:
        return units[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 70:
        ten = n // 10
        unit = n % 10
        if unit == 0:
            return tens[ten]
        else:
            return f"{tens[ten]} {units[unit]}"
    else:
        return str(n)


def get_hour_text(n: int, context: str = "remaining") -> str:
    """
    context:
      - “remaining”: nominative case (remaining)
      - “started”: accusative case (started on)
    """
    if context == "remaining":

        if 11 <= n % 100 <= 14:
            return "годин"
        last = n % 10
        if last == 1:
            return "година"
        elif 2 <= last <= 4:
            return "години"
        else:
            return "годин"
    elif context == "started":

        if 11 <= n % 100 <= 14:
            return "годин"
        last = n % 10
        if last == 1:
            return "годину"
        elif 2 <= last <= 4:
            return "години"
        else:
            return "годин"

def get_minute_text(n: int, context: str = "remaining") -> str:

    if context == "remaining":
        if 11 <= n % 100 <= 14:
            return "хвилин"
        last = n % 10
        if last == 1:
            return "хвилина"
        elif 2 <= last <= 4:
            return "хвилини"
        else:
            return "хвилин"
    elif context == "started":
        if 11 <= n % 100 <= 14:
            return "хвилин"
        last = n % 10
        if last == 1:
            return "хвилину"
        elif 2 <= last <= 4:
            return "хвилини"
        else:
            return "хвилин"

def get_second_text(n: int, context: str = "remaining") -> str:

    if context == "remaining":
        if 11 <= n % 100 <= 14:
            return "секунд"
        last = n % 10
        if last == 1:
            return "секунда"
        elif 2 <= last <= 4:
            return "секунди"
        else:
            return "секунд"
    elif context == "started":
        if 11 <= n % 100 <= 14:
            return "секунд"
        last = n % 10
        if last == 1:
            return "секунду"
        elif 2 <= last <= 4:
            return "секунди"
        else:
            return "секунд"


def format_time_text(minutes: int, seconds: int = 0, context: str = "remaining"):
    hours = minutes // 60
    mins = minutes % 60

    parts_text = []
    parts_tts = []

    case = "acc" if context == "started" else "nom"

    if hours > 0:
        hour_word = get_hour_text(hours, context)
        hour_text = number_to_words_uk(hours, gender="f", case=case)
        parts_text.append(f"{hours} {hour_word}")
        parts_tts.append(f"{hour_text} {hour_word}")

    if mins > 0:
        min_word = get_minute_text(mins, context)
        min_text = number_to_words_uk(mins, gender="f", case=case)
        parts_text.append(f"{mins} {min_word}")
        parts_tts.append(f"{min_text} {min_word}")

    if seconds > 0:
        sec_word = get_second_text(seconds, context)
        sec_text = number_to_words_uk(seconds, gender="f", case=case)
        parts_text.append(f"{seconds} {sec_word}")
        parts_tts.append(f"{sec_text} {sec_word}")

    if not parts_text:
        parts_text.append("0 хвилин")
        parts_tts.append("нуль хвилин")

    return " ".join(parts_text), " ".join(parts_tts)


def get_verb_for_remaining(hours: int, minutes: int, seconds: int) -> str:

    if hours > 0:
        number = hours
    elif minutes > 0:
        number = minutes
    else:
        number = seconds

    last_two = number % 100
    last = number % 10

    if last_two >= 11 and last_two <= 14:
        return "залишилось"
    if last == 1:
        return "залишилась"
    else:
        return "залишилось"