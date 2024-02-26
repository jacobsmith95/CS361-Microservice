# Microservice Code by Jacob Smith
# A program that returns a set of staple cards based on the input colors sent by a main program
# CS361


import sys
import socket
import json
import itertools


def main():
    """function which runs the microservice, keeping it always on and waiting for import"""

    staple_array = import_staple_array()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = "127.0.0.1"

    server_socket.bind((address, 54345))

    server_socket.listen(5)

    print(f"Server listening on port 54345...\n")

    while True:

        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        try:
            message = client_socket.recv(1024)
            print(f"Client Message: {message.decode()}")

            response = "Staples\n\n"
                
            if message.decode() == "end":
                response = "Server Ending"
                client_socket.sendall(response.encode())
                server_socket.close()
                sys.exit()

            if message.decode() == "None":
                response = "No client input!"
                print("No client input...")

            else:
                client_message = message.decode()
                orig_list = list(client_message.split(" "))

                if "c" in orig_list:
                    colorless_list = return_colorless_staples(staple_array)
                    colorless_str = stringify_staples(colorless_list)
                    response += colorless_str
                    response += "\n\n"
                    orig_list.remove("c")

                combo_list = find_combinations(orig_list)

                user_list = convert_to_index(combo_list)

                single_str = find_staples(user_list, staple_array)
                response += single_str
                response += "\n\n"



            client_socket.sendall(response.encode())

        finally:
            client_socket.close()



def import_staple_array() -> list:
    """function that opens the staple card json and returns a list of dictionaries of staple cards per color"""
    staple_file = open("staples.json", "r")
    staples = json.load(staple_file)
    staple_array = staples["Colors"]
    staple_file.close()
    return staple_array


def find_combinations(user_list) -> list:
    """finds all unique variations of the user's chosen colors"""

    array = []

    for i in range(1, len(user_list) + 1):
        array.append(list(itertools.combinations(user_list, i)))

    for i in range(len(array)):
        for x in range(len(array[i])):
            array_str = ""
            for y in range(len(array[i][x])):
                array_str += array[i][x][y]
            array[i][x] = array_str

    result = []
    for i in range(len(array)):
        result.extend(array[i])

    return result


def convert_to_index(user_list) -> list:
    """converts the user string list to a list of numbers to use as indices"""
    for i in range(len(user_list)):
        match user_list[i]:
            case "w":
                user_list[i] = 1
            case "u":
                user_list[i] = 2
            case "b":
                user_list[i] = 3
            case "r":
                user_list[i] = 4
            case "g":
                user_list[i] = 5
            case "wu":
                user_list[i] = 6
            case "ub":
                user_list[i] = 7
            case "br":
                user_list[i] = 8
            case "rg":
                user_list[i] = 9
            case "wg":
                user_list[i] = 10
            case "wb":
                user_list[i] = 11
            case "ur":
                user_list[i] = 12
            case "bg":
                user_list[i] = 13
            case "wr":
                user_list[i] = 14
            case "ug":
                user_list[i] = 15
            case "wub":
                user_list[i] = 16
            case "ubr":
                user_list[i] = 17
            case "brg":
                user_list[i] = 18
            case "wrg":
                user_list[i] = 19
            case "wug":
                user_list[i] = 20
            case "wbg":
                user_list[i] = 21
            case "wur":
                user_list[i] = 22
            case "ubg":
                user_list[i] = 23
            case "wbr":
                user_list[i] = 24
            case "urg":
                user_list[i] = 25
            case "wubr":
                user_list[i] = 26
            case "ubrg":
                user_list[i] = 27
            case "wubg":
                user_list[i] = 28
            case "wurg":
                user_list[i] = 29
            case "wbrg":
                user_list[i] = 30
            case "wubrg":
                user_list[i] = 31
    return user_list


def return_colorless_staples(staple_array) -> list:
    """returns colorless staple cards from the staple array"""
    colorless_list = []
    colorless_dict = staple_array[0]
    colorless_list.extend(colorless_dict["staples"])
    colorless_list.insert(0, "Colorless:")
    return colorless_list


def find_staples(user_list, staple_array) -> str:
    """finds all single colors in the user color list and outputs their staple cards"""

    staple_str = ""

    for element in user_list:
        color_str = ""
        card_array = []
        color_dict = staple_array[element]
        card_array.extend(color_dict["staples"])
        if type(color_dict["color"]) is list:
            color_str = "/".join(color_dict["color"])
            color_str = color_str + ":"
        else:
            color_str = color_dict["color"]
            color_str = color_str + ":"
        card_array.insert(0, color_str)
        add_str = stringify_staples(card_array)
        staple_str += add_str
        staple_str += "\n\n"

    return staple_str


def stringify_staples(staple_list) -> str:
    """function that takes a staple list and returns a string with those staples in a nice, easy-to-read format"""
    return_str = "\n".join(staple_list)
    return return_str


if __name__ == "__main__":
    main()