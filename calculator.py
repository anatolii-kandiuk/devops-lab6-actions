class WeightConverter:    
    GRAMS_IN_KG = 1000
    GRAMS_IN_TONNE = 1000000
    
    @staticmethod
    def grams_to_kilograms(grams: float) -> float:
        return grams / WeightConverter.GRAMS_IN_KG
    
    @staticmethod
    def grams_to_tonnes(grams: float) -> float:
        return grams / WeightConverter.GRAMS_IN_TONNE
    
    @staticmethod
    def kilograms_to_grams(kilograms: float) -> float:
        return kilograms * WeightConverter.GRAMS_IN_KG
    
    @staticmethod
    def kilograms_to_tonnes(kilograms: float) -> float:
        return kilograms / 1000
    
    @staticmethod
    def tonnes_to_grams(tonnes: float) -> float:
        return tonnes * WeightConverter.GRAMS_IN_TONNE
    
    @staticmethod
    def tonnes_to_kilograms(tonnes: float) -> float:
        return tonnes * 1000


def main():
    converter = WeightConverter()
    
    print("Weight Converter")
    print("=" * 40)
    
    grams = 5000
    print(f"{grams} grams = {converter.grams_to_kilograms(grams)} kg")
    print(f"{grams} grams = {converter.grams_to_tonnes(grams)} tonnes")
    
    kg = 2.5
    print(f"{kg} kg = {converter.kilograms_to_grams(kg)} grams")
    print(f"{kg} kg = {converter.kilograms_to_tonnes(kg)} tonnes")
    
    tonnes = 1.5
    print(f"{tonnes} tonnes = {converter.tonnes_to_grams(tonnes)} grams")
    print(f"{tonnes} tonnes = {converter.tonnes_to_kilograms(tonnes)} kg")

if __name__ == "__main__":
    main()
