import os
# Faylları uzantılarına görə qovluqlar yaradıb yerləşdirmək
def repair():
    folder = input("Qovluqun olduğu yeri daxil edin : ")
    try:
        extensions = []
        files = []
        # Qovluqda olan faylları və ya qovluqları listliyib, qovluqdusa və gizli fayldısa alma ,qalanını göndər files-a.
        def list_dir():
            for file in os.listdir(folder):
                if os.path.isdir(os.path.join(folder,file)):
                    continue
                if file.startswith("."):
                    continue
                else:
                    files.append(file)

        list_dir()
        #Faylların uzantılarını alma
        for file in files:
            extension =file.split(".")[-1]
            if extension in extensions:
                continue
            else:
                extensions.append(extension)

    #Uzantılara məxsus dosyalar yaratdım və təkrarlanmanın qarşısını aldım
        for extension in extensions :
            if os.path.isdir(os.path.join(folder,extension)):
                continue
            else:
                os.mkdir(os.path.join(folder,extension))
        #Yaratdıgım uzantı qovluqlarına həmin uzantılı faylları göndərdim
        for file in files:
            extension = file.split(".")[-1]
            os.rename(os.path.join(folder,file),os.path.join(folder,extension,file))
        print("Tamamlandı")
    except:
        print("Yalnış qovluq yolu")
if __name__ =="__main_-":
    repair()

repair()