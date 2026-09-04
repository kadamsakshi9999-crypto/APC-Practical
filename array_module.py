from array import array

# 1. append()
a = array('i', [10, 20, 30])
a.append(40)
print("append():", a)


# 2. buffer_info()
a = array('i', [10, 20, 30])
print("buffer_info():", a.buffer_info())


# 3. byteswap()
a = array('i', [1, 2, 3])
a.byteswap()
print("byteswap():", a)


# 4. count()
a = array('i', [10, 20, 10, 30, 10])
print("count():", a.count(10))


# 5. extend()
a = array('i', [10, 20])
a.extend([30, 40])
print("extend():", a)


# 6. frombytes()
a = array('i', [10, 20])
b = array('i')
b.frombytes(a.tobytes())
print("frombytes():", b)


# 7. fromfile()
a = array('i', [10, 20, 30])
with open("numbers.bin", "wb") as f:
    a.tofile(f)

b = array('i')
with open("numbers.bin", "rb") as f:
    b.fromfile(f, 3)

print("fromfile():", b)


# 8. fromlist()
a = array('i')
a.fromlist([10, 20, 30])
print("fromlist():", a)


# 9. fromunicode()
a = array('u')
a.fromunicode("Hello")
print("fromunicode():", a)


# 10. index()
a = array('i', [10, 20, 30, 40])
print("index():", a.index(30))


# 11. insert()
a = array('i', [10, 20, 40])
a.insert(2, 30)
print("insert():", a)


# 12. pop()
a = array('i', [10, 20, 30])
x = a.pop()
print("Removed:", x)
print("pop():", a)


# 13. remove()
a = array('i', [10, 20, 30, 20])
a.remove(20)
print("remove():", a)


# 14. reverse()
a = array('i', [10, 20, 30, 40])
a.reverse()
print("reverse():", a)


# 15. tobytes()
a = array('i', [10, 20, 30])
data = a.tobytes()
print("tobytes():", data)


# 16. tofile()
a = array('i', [10, 20, 30])
with open("numbers.bin", "wb") as f:
    a.tofile(f)
print("Data written to file")


# 17. tolist()
a = array('i', [10, 20, 30])
print("tolist():", a.tolist())


# 18. tounicode()
a = array('u', 'Hello')
print("tounicode():", a.tounicode())
