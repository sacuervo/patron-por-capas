# main.py
from data_layer import DataLayer
from business_layer import BusinessLayer
from presentation_layer import PresentationLayer

def main():
    data_layer = DataLayer()
    business_layer = BusinessLayer(data_layer)
    presentation_layer = PresentationLayer(business_layer)

    presentation_layer.show_menu()

if __name__ == "__main__":
    main()
