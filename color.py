def format_color(text, color):
    return f"{color}{text}{Color.end_color_format}"

class Color:
    def color(color_code):
        return f"\x1b[{color_code}m"
    
    red = color("0;31;40")
    green = color("0;32;40")
    yellow = color("0;33;40")
    blue = color("0;34;40")

    end_color_format = '\x1b[0m'


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

if __name__ == "__main__":
    print_format_table()