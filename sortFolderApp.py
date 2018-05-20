import os
import glob
import shutil
import random

#データセットフォルダ名、トレインフォルダ名、バリデーションフォルダ名を設定。
path = os.path.dirname(os.path.abspath(__file__))
dataset_dir = "dataset"
train_dir = "dataset\\train"
validation_dir = "dataset\\validation"

#トレイン、バリデーションの振り分け率
#4だったら、トレイン3:バリデーション1の割合
DistributionRatio = 4 

def getFolder():
    """
    フォルダ
    """
    #フォルダ名を取得。
    files = os.listdir(path)
    folder_list = [f for f in files if os.path.isdir(os.path.join(path, f))]
    
    #datasetフォルダを除外する。
    try:
        folder_list.remove("dataset")
    except:
        pass

    #データを格納するフォルダを作成
    if not os.path.exists(dataset_dir):
        os.mkdir(dataset_dir)
    if not os.path.exists(train_dir):
        os.mkdir(train_dir)
    if not os.path.exists(validation_dir):
        os.mkdir(validation_dir)
    
    #フォルダのコピー
    for folderName in folder_list:
        results = listSort(folderName)
        train_data = results[0]
        validation_data = results[1]
        filecopy(folderName, train_data, validation_data)

def listSort(folderName):
    """
    フォルダ名からファイルをコピーする。
    """
    files = os.listdir(os.path.join(path, folderName))
    # print(files)
    file_list = [f for f in files if os.path.isfile(os.path.join(path, folderName, f))]
    #シャッフル
    random.shuffle(file_list)
    validate_list = []
    train_list = []

    #ファイル名をトレイン用テスト用に分ける。
    for index, file_name in enumerate(file_list):
        if index % DistributionRatio == 0:
            validate_list.append(file_name)
        else:
            train_list.append(file_name)
    
    return (train_list, validate_list)


def filecopy(dirName, trainList, validationList):
    """
    ファイル名からトレイン、バリデーションフォルダにコピーする。
    """
    #フォルダの作成。
    if not os.path.exists(os.path.join(path, train_dir, dirName)):
        os.mkdir(os.path.join(path, train_dir, dirName))
    
    if not os.path.exists(os.path.join(path, validation_dir, dirName)):
        os.mkdir(os.path.join(path, validation_dir, dirName))
    
    #コピーを実行。
    for tFile in trainList:
        orignal = os.path.join(path, dirName, tFile)
        copyTo = os.path.join(path, train_dir, dirName, tFile)
        shutil.copy(orignal, copyTo)
        print("orignal:{0}_copyTo:{1}".format(orignal, copyTo))

    for tFile in validationList:
        orignal = os.path.join(path, dirName, tFile)
        copyTo = os.path.join(path, validation_dir, dirName, tFile)
        shutil.copy(orignal, copyTo)
        print("orignal:{0}_copyTo:{1}".format(orignal, copyTo))

if __name__ == '__main__':

    getFolder()
