a = [1, 3, 5, 2312, 231, 12, 3, 312, 3121 , 42, 412, 312]

# print(a)
# print(type(a))
# print(max(a))


def myMax(elements):
    if len(elements) == 0:
        return None
    else:
        m = elements[0]

        # for element in elements[1:]:
        #     if element > m:
        #         m = element
        
        i = 1
        while i < len(elements):
            if elements[i] > m:
                m = elements[i]
            i += 1

        return m


print(myMax(a))