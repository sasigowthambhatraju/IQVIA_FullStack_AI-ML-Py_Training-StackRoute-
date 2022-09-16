from sklearn import tree

predictions = open("predictions.txt", 'w+')
predictions.write("100,0,103,0,140,0,150,1,160,1,200,1")
predictions.write("\n0,0,0,1,1,1")
predictions.close()

def training():
    try:
        weight = int(input("Please enter weight: "))
        texture = int(input("Please eter texture 0 or 1, 0 for rough & 1 for smooth: "))
        label = int(input("Please enter label 0 or 1, 0 for orange & 1 for apple: "))
        file = open("predictions.txt", 'r')
        features = file.readline().strip('\n').split(',')
        labels = file.readline().split(',')
        file.close()

        features.extend([weight, texture])
        labels.append(label)

        with open("predictions.txt", 'w') as f2:
            for feature in features:
                f2.write('%s,' %feature)
            f2.write('\n')
            for label in labels:
                f2.write('%s,'%label)
            f2.close()
            print("New data have been appended..")
    except Exception as ex:
        print(ex)

# def predict():
#     try:
#         file = open("predictions.txt", 'r')
#         features = file.readline().strip('\n').split(',')
#         labels = file.readline().split(',')
#         file.close()
#
#         features = ' '.join(features).split()
#         labels = ' '.join(labels).split()
#

