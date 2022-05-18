import os
if __name__ == '__main__':
    textcolors = {'gray' : 90, 'red' : 91, 'green' : 92, 'yellow' : 93, 'blue' : 94, 'pink':95, 'cyan':96}
    bgcolors = {'gray' : 100, 'red' : 101, 'green' : 102, 'yellow' : 103, 'blue' : 104, 'pink':105, 'cyan':106}
    styles = {
    'Reset / Normal        ' : 0 ,
    'Bold/increased intense' : 1 ,
    'Faint (less intense)  ' : 2 ,
    'Italic                ' : 3 ,
    'Underline             ' : 4 ,
    'Slow Blink            ' : 5 ,
    'Rapid Blink           ' : 6 ,
    'reverse video         ' : 7 ,
    'Conceal               ' : 8 ,
    'Crossed-out           ' : 9 ,
    'Primary(default) font ' : 10,
    'Alternate font 1      ' : 11,
    'Alternate font 2      ' : 12,
    'Alternate font 3      ' : 13,
    'Alternate font 4      ' : 14,
    'Alternate font 5      ' : 15,
    'Alternate font 6      ' : 16,
    'Alternate font 7      ' : 17,
    'Alternate font 8      ' : 18,
    'Alternate font 9      ' : 19,
    'Fraktur               ' : 20,
    'Bold/Double Uline off ' : 21,
    'Normal color+intensity' : 22,
    'Not italic not Fraktur' : 23,
    'Underline off         ' : 24,
    'Blink off             ' : 25,
    'Inverse off           ' : 27,
    'Reveal                ' : 28,
    'Not crossed out       ' : 29,
    'Set foreground color1 ' : 30,
    'Set foreground color2 ' : 31,
    'Set foreground color3 ' : 32,
    'Set foreground color4 ' : 33,
    'Set foreground color5 ' : 34,
    'Set foreground color6 ' : 35,
    'Set foreground color7 ' : 36,
    'Set foreground color8 ' : 37,
    'Set foreground color9 ' : 38,
    'Default foreground color' : 39,
    'Set background color 1' : 40,
    'Set background color 2' : 41,
    'Set background color 3' : 42,
    'Set background color 4' : 43,
    'Set background color 5' : 44,
    'Set background color 6' : 45,
    'Set background color 7' : 46,
    'Set background color 8' : 47,
    'Set background color 9' : 48,
    'Default backgroundcolor' : 49,
    'Framed                ' : 51,
    'Encircled             ' : 52,
    'Overlined             ' : 53,
    'Not framed/encircled  ' : 54,
    'Not overlined         ' : 55,
    'ideogram underline    ' : 60,
    'ideogram dbl underline' : 61,
    'ideogram overline     ' : 62,
    'ideogram dbl overline ' : 63,
    'ideogram stress markin' : 64,
    'ideogram attributes off' : 65
    }



    os.system("clear")


    print('''SYNTAX HELP

    ANSI
    __________________________________________________________________________________
            
        \033[101m\ \033[0m0 3 3 \033[104m[ \033[0m1 0 2 m
    __________________________________________________________________________________
    \033[101m  \033[0m  -- escape sequence \\033 for python
    \033[104m  \033[0m  -- escape for attribute index
    m  -- signifies that the code is over
    033 -- is the unique python identifier
    102 -- is the unique attribute code for the color green
    ''')


    def bgcolor(name):
        name = f'{name}'
        bgcolorr = "\\033[" + str(bgcolors[f'{name}']) + "m"
        print(f"  {name} = " + bgcolorr)

    def fgcolor(name):
        name = f'{name}'
        fgcolorr = "\\033[" + str(textcolors[f'{name}']) + "m"
        print(f"  {name} = " + fgcolorr)

    def style(name):
        name = f'{name}'
        styler = "\\033[" + str(styles[f'{name}']) + "m"
        print(f"  {name}" + " = " + styler)
    ###########################################################

    fgcolors_list = []
    print(f"#\033[104m                                     Text Colors codes             <<\033[0m ")
    for item in textcolors:
        fgthing = fgcolor(item)
        fgcolors_list.append(fgthing)


    bgcolors_list = []
    print(f"\n#\033[102m                                      Background Colors codes      <<\033[0m ")
    for item in bgcolors:
        bgthing = bgcolor(item)
        bgcolors_list.append(bgthing)

    print(f'\033[7m#                              All three digit codes for Attributes <<\033[0m')
    stylelist = []
    for item in styles:
        if item == 'Primary(default) font ':
            print('')
            print("# \033[106m                                  ALT Fonts codes                 <<\033[0m")
        elif item == 'Set foreground color1 ':
            print(f'\n#\033[105m                                   FG/BG Defaults codes          <<\033[0m')
        elif item == 'Framed                ':
            print(f'\n#\033[103m                                   Frames  codes               <<\033[0m')
        stylerthing = style(item)
        stylelist.append(stylerthing)


    print(f'\n\033[3m \033[106m [ copy and paste variables list ] \033[0m')
    print('''
    _gray = '\\033[90m
    _red = '\\033[91m
    _green '= \\033[92m
    _yellow '= \\033[93m
    _blue = '\\033[94m
    _pink = '\\033[95m
    _cyan = '\\033[96m
    bg_gray = '\\033[100m'
    bg_red = '\\033[101m'
    bg_green = '\\033[102m'
    bg_yellow = '\\033[103m'
    bg_blue = '\\033[104m'
    bg_pink = '\\033[105m'
    bg_cyan = '\\033[106m'
    END = '\\033[0m'
    _bold = '\\033[1m'
    _dim = '\\033[2m'
    _italic = '\\033[3m'
    _underline = '\\033[4m'
    _slowblink = '\\033[5m'
    _fastblink = '\\033[6m'
    _reverse = '\\033[7m'
    _conceal = '\\033[8m'
    _crossedout = '\\033[9m'

    ''')

    print('''
    \033[6m>\033[5m\033[6m>\033[0m \033[6m       EXAMPLE OF F-STRING\033[0m\n
    \033[7m\033[92m\033[3m[  Code Editor  ]\033[0m\033[7m
    BoldGreenOnPink = _green + bg_pink + _bold                       0
    mystring = f' {BoldGreenOnPink} hello! {_end} '                  1
    print ( mystring )                                               2
    \n\033[0m 
    looks like ...

    \033[92m\033[105m\033[1m hello! \033[0m
    _____________________________________________''')

