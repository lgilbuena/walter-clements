
if __name__ == '__main__':
    lines = ['pog','sheep']
    with open('userIDS.txt','w') as f:
        for l in lines:
            f.write(l)