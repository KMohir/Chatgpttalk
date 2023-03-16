import easyocr


def text_recognition(path_file,file_txt="result.txt"):
    # path_file="EasyOCR\examples\english.png"
    reading=easyocr.Reader(["en"])
    result=reading.readtext(path_file,detail=False,paragraph=True)

    with open(file_txt,"w") as file:
        for line in result:
            file.write(f"{line}\n")
    return f"{result}"

def main():
    file_path= "pictranslate/test.jpg"
    a=text_recognition(file_path)
    return a

main()
