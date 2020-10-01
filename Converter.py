import PySimpleGUI as sg

sg.theme('Topanga')
layout = [[(sg.Text('Napiš \nBinToDec/DecToBin/DecToHex/HexToDec/BinToHex/HexToBin/BinToText/TextToBin/HexToText/TextToHex\npro převod z dané soustavy.', size=[80, 3]))],
            [sg.InputText(size=(40, 1), do_not_clear=False)],
            [sg.Text('Sem napiš své číslo:', size=(40, 1))],
            [sg.InputText(size=(40, 1),do_not_clear=False)],
            [sg.Multiline(size=(80,15), auto_refresh=True, reroute_stdout=True, reroute_cprint=True, disabled=True, autoscroll=True)],
            [sg.Button('OK',bind_return_key=True),
            sg.Button('Exit')]]

window = sg.Window('Convertor 1.0.0', layout, default_element_size=(30, 2))

def restartf():
    while True:

        event, value = window.read()
        
        if event == 'OK':


            if value[0] != "Help":
                if value[1] == '':
                    print("Musíš napsat číslo na konvertování!")
                    restartf()
            if value[0] == "BinToDec":
                def bindec(n): 
                    return int(n, 2)
                input1 = value[1]
                print("Tvé číslo z", value[0], "je", bindec(input1), "\n")


            elif value[0] == "DecToBin":
                def decbin(n): 
                    return bin(n).replace("0b","")
                input1 = int(value[1])
                print("Tvé číslo z", value[0], "je", decbin(input1), "\n")

            elif value[0] == "HexToDec":
                input1 = value[1]
                vysledek = int(input1, 16)
                print("Tvé číslo z", value[0], "je", vysledek)

            elif value[0] == "DecToHex":
                input1 = int(value[1])
                print("Tvé číslo z", value[0], "je", hex(input1).replace("0x",""), "\n")

            elif value[0] == "HexToBin":
                input1 = value[1]
                vysledek = int(input1, 16)
                def decbin(n): 
                    return bin(n).replace("0b","")
                vysledekbin = decbin(vysledek)
                print("Tvé číslo z", value[0], "je", vysledekbin, "\n")
            
            elif value[0] == "BinToHex":
                def bindec(n): 
                    return int(n, 2)
                input1 = value[1]
                bide = bindec(input1)
                print("Tvé číslo z", value[0], "je", hex(bide).replace("0x",""), "\n")

            elif value[0] == "BinToText":

                input1 = value[1]
                def decode_binary_string(s):
                    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
                print(decode_binary_string(input1))

            elif value[0] == "TextToBin":
                input1 = value[1]
                print("Tvé číslo je:\n",''.join('{:08b}'.format(d) for d in bytearray(input1, 'utf-8')), "\n")
            
            elif value[0] == "TextToHex":
                input1 = value[1]
                textbin = ''.join('{:08b}'.format(d) for d in bytearray(input1, 'utf-8'))
                def bindec(n): 
                    return int(n, 2)
                bide = bindec(textbin) 
                print("Tvé číslo je:\n",hex(bide).replace("0x",""), "\n")

            elif value[0] == "HexToText":
                input1 = value[1]
                vysledek = int(input1, 16)
                def decbin(n): 
                    return bin(n).replace("0b","")
                bide = decbin(vysledek)
                def decode_binary_string(s):
                    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
                print("Tvůj text je:\n",decode_binary_string("0" + bide), "\n")

            elif value[0] == "Help":
                print("BinToDec\n   Z binární soustavy do decimální")
                print("DecToBin\n   Z decimální soustavy do binární")
                print("BinToHex\n   Z binární soustavy do hexadecimální")
                print("HexToBin\n   Z hexadecimální soustavy do binární")
                print("DecToHex\n   Z decimální soustavy do hexadecimální")
                print("HexToDec\n   Z hexadecimální soustavy do decimální")
                print("BinToText\n   Z binární soustavy do textu")
                print("TextToBin\n  Z textu do binární soustavy")
                print("HexToText\n  Z hexadecimální soustavy do textu")
                print("TextToHex\n  Z textu do hexadecimální soustavy")
            else:
                print("Nemám tenhle příkaz.")
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            break
    
    window.close()
restartf()
