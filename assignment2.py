def menu():
    print('1. Enter the list of integer number: ')
    print('2. Search for a value in a list entered by the user: ')
    print('3. Print out the element with the largest value in the list: ')
    print('4. Remove the element whose value is equal to the value entered by the user:')
    print('5. print out the list in ascending order ')
    print('6. Others-Quit')


def value_input(data,count):
    while True:
        try:
            num = int(input('entering number: '))
            if num == 0 or count == 100:
                print('existing..........')
                break
            else:
                data.append(num)
                count += 1
                print('number enter successfully')
        except:
            print('invalid input')
    return data

def search_number(data,value):
    result = 0
    print(data)
    for i in data :
        if value == data[i]:
            print('there is ', value, ' in the string' )
        i += 1
        result = 1
    if result == 0 :
        print('there is not ', value,'in the string')


def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for num in data:
        if num > largest:
            largest = num
    return largest


def remove_number(data,value):
    try:
        data.remove(value)
        return True
    except ValueError:
        return False


def main():
    while True:
        data = []
        count = 0
        menu()
        try:
            choose = input('enter your command: ')
            if choose == '1':
                print('enter the number to append to list or 0 to break')
                value_input(data,count)
            elif choose == '2':
                value = int(input('enter data for searching'))
                search_number(data,value)
            elif choose == '3':
                largest = find_largest(data)
                if largest is None:
                    print('list is empty ')
                else: print('largest number is: ',largest )
            elif choose == '4':
                input('enter the number for removing: ')
                if not data:
                    print('the list is empty')
                else :
                    value  = input(int('enter the number for removing: '))
                    remove = remove_number(data, value)
                    if remove:
                        print('element remove successfully ')
                    else:
                        print('element not found')
            elif  choose == '5':
                print('data list', data)
            elif choose == '6':
                print('existing program.... ')
                break
        except:
            print('invalid choice')

if __name__ := '__main__':
    main()
