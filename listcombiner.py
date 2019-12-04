def filecombiner():
    files = ['paginalijst1.txt', 'paginalijst2.txt', 'paginalijst3.txt', 'paginalijst4.txt', 'paginalijst5.txt',
             'paginalijst6.txt', 'paginalijst7.txt', 'paginalijst8.txt', 'paginalijst9.txt', 'paginalijst10.txt',
             'paginalijst11.txt', 'paginalijst12.txt', 'paginalijst13.txt', 'paginalijst14.txt', 'paginalijst15.txt',
             'paginalijst16.txt', 'paginalijst17.txt', 'paginalijst18.txt', 'paginalijst19.txt', 'paginalijst20.txt',
             'paginalijst21.txt', 'paginalijst22.txt', 'paginalijst23.txt', 'paginalijst24.txt', 'paginalijst25.txt']

    with open('paginalijst-combined.txt', 'w') as outfile:
        for filename in files:
            with open(filename) as infile:
                outfile.write(infile.read())

    # Test to count rows in file
    # with open('paginalijst-uniques.txt', 'r') as outfile:
    #     count = 0
    #     for url in outfile:
    #         count += 1
    #         print(count)


if __name__ == "__main__":
    filecombiner()