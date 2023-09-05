def pyramid(n):
    ip = n
    space = int(ip)
    for r in range(1,ip+1):
        for s in range(space*2):
                print (end=" ")    
        space = space-1

        for c in range(1,r+1):
                print (str(c) + "  ",end="")
        print ("\n")


def main():
    pyramid(5)

if __name__ == "__main__":
    main()
