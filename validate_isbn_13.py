from faker import Faker


for i in range(1000000):
    Faker.seed(i)
    fake = Faker()
    check = fake.isbn13()
    print(check)
    check = check.split("-")
    result = int(''.join(map(str, check[4])))

    if check[0]=='978' or check[0]=='979':
        if 1 >= len(check[1]) <= 5:
            if len(check[2]) >= 1 and len(check[2]) <= 7:
                if len(check[3]) >= 1 and len(check[3]) <= 6:
                    if len(check[4])==1 and type(result) == int:
                        print('Generation is OK')
                    else:
                        print("Error4")
                else:
                    print("Error3")
            else:
                print("Error2")
        else:
            print("Error1")
    else:
        print("Error0")