import json
from projekt import Ship, Matrix, PilotageMap, DraftValueError, MatrixSizeError, MatrixError

#Below enter path to file 'information.json', remember to put it in " " 
ourpath = "/home/kacper/pipr/labki/Projekt/information.json"


def main(path):
    try:
        with open(path, "r") as file_handle:
                data=json.load(file_handle)
                OurShip = Ship(data["draft"])
                OurMatrix = Matrix(data["size"],data["matrix_with_heights"])
                OurMap = PilotageMap(OurShip, OurMatrix)
                print(OurMap.show_map())
    except (DraftValueError, MatrixSizeError, MatrixError) as e:
        print(str(e))
    except json.JSONDecodeError:
        print('Wrong value in file')
    except FileNotFoundError:
        print('Wrong file path')


if __name__ == "__main__":
    main(ourpath)