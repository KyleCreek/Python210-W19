class FileProcessor:
    """ This class processes data to and from files  """

    @staticmethod
    def filewriter(file: str, data: str, append: bool = True) -> None:
        """ Desc: Writes data to a file
        :param file: string with file name
        :param data: data to write
        :param append:boolean defining append or overwrite option
        :return: None
        """
        if append: mode = 'a'
        else: mode = 'w'
        objFile = open(file, mode)
        objFile.write(data + '\n')
        objFile.close()

    @staticmethod
    def filereader(file: str) -> list:
        """ Desc: Reads data from a file
        :param file: string with file name
        :return: list of string data
         :rtype: list
        """
        lstData = []
        objFile = open(file)
        for value in objFile:
            lstData.append(value.replace('\n',''))
        objFile.close()
        return lstData

# ------------------------
# FileProcessor.filewriter("textdata.txt","Test1:Passed")
# data = FileProcessor.filereader("textdata.txt")
# print(data)
