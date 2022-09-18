# var = input('напиши')
# fw = open("doc/file.txt", 'a')
# fw.write(var)
# fw.close()


# fw = open("doc/file2.txt", 'w')
# fw.write('privetiiiii')
# fw.close()

# fa = open('doc/file.txt')
# text = fa.read()
# fa.close()
# print(text)

# file = open('doc/test.txt', 'w') # Используем функцию open с режимом "w"
# file.write("Hello world!") # Метод write(текст) для записи в файл
# file.close() # Обязательно закрыть файл в конце

"""С этим способом можно не закрывать файл явно, 
он закроется автоматически, 
когда программа выйдет из блока with."""

with open('doc/test.txt', 'w+') as file:
    file.write("Hello world!")
