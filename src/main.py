from layers.bronze import bronze_layer_processing
from layers.silver import silver_layer_processing
from layers.gold import gold_layer_processing

def main():
    bronze_layer_processing()
    silver_layer_processing()
    gold_layer_processing()

if __name__ == "__main__":
    main()