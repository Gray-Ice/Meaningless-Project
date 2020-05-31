import os
import arrow


class FileChange(object):
    """
    file_list will return a list, and "change_keyword.py" won't in it.
    change_file will change data.You should have a good think before use it.
    do_it will use file_list and change_file to change every file in this directory.
    """

    def __init__(self, old_word, new_word, max_range):
        """

        :param old_word: Old word.
        :param new_word: New word.
        :param max_range: the number that you want to instead in every file.
        """
        self.old_word = old_word
        self.new_word = new_word
        self.path = os.path.abspath('') + '\\'
        self.max_range = int(max_range)
        self.success_list = []

    def file_list(self):
        """
        This class function will return a list.
        :return: It will return a list without "change_keyword.py".
        """
        fns = os.listdir()
        if os.path.basename(__file__) in fns:
            fns.remove(os.path.basename(__file__))
        return fns

    def back_up(self, filedata, filename):
        """
        To back-up the success file.
        :param filedata: The data of your file.
        :param filename: The name of your file.
        :return: Success status.
        """
        try:
            os.mkdir(self.path + 'back-up')
        except FileExistsError:
            pass
        with open('./back-up/' + filename, 'w') as f:
            f.write(filedata)
        return filename + 'was back up in directory back-up'

    def change_file(self, filename):
        """
        :param filename:  The file which will be changed.
        :return: Return the result, not matter it was success or defeat.
        """
        if filename.endswith('.txt') or filename.endswith('.md'):

            with open(self.path + filename, 'r') as f:
                file_msg = f.read()

            if self.old_word in file_msg:
                print(self.back_up(filedata=file_msg, filename=filename))
                if self.max_range:
                    file_msg = file_msg.replace(self.old_word, self.new_word, self.max_range)
                else:
                    file_msg = file_msg.replace(self.old_word, self.new_word)

                with open(self.path + filename, 'w') as f:
                    f.write(file_msg)

                self.success_list.append(filename)
                return 'Success！The file name is :' + filename
            else:
                return 'Here is no keyword.'
        else:
            return 'This is not the right type.'

    def make_success_file(self):
        """
        To make a success list in ./backup/success.txt .
        :return: 0
        """
        with open('./back-up/success_file_list.txt', 'a') as f:
            f.write(arrow.now().format('YYYY-MM-DD HH:mm') + '\n')
            f.write(str(self.success_list))
            f.write('\n\n')
        return 'Made a success list file in ./back-up/success_file_list.txt'

    def do_it(self):
        """
        In order to change every file in this directory.
        """
        for file in self.file_list():
            print(self.change_file(file))
        if len(self.success_list):
            print('This is success list: ', self.success_list)
            print(self.make_success_file())
        else:
            print('Nothing changed.')
        return 0


def main():
    old_word = input('Please enter your old word')
    new_word = input('Please enter your new word')
    max_range = input(
        'Please enter the number that you want to change in every file.'
        'If you enter a string, this program will change every string accord with the old word and the new word \n')
    if old_word == '':
        print("Old keyword can't be null, please have a good think.")
        print('for disabling the old keyword, input it into "old word", and press Enter at "new word"')
        input('Press any key and press enter to close this window')
        return 0
    if max_range.isalnum():
        file = FileChange(old_word=old_word, new_word=new_word, max_range=max_range)
        file.do_it()
    else:
        file = FileChange(old_word=old_word, new_word=new_word, max_range=0)
        file.do_it()
    input('Press enter to close this window.')


if __name__ == '__main__':
    main()
