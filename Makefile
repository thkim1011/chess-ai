SRC_DIR = src
INCLUDE_DIR = include
BUILD_DIR = build
BIN_DIR = bin

all: $(BUILD_DIR)/chess.o $(BUILD_DIR)/main.o
	g++ $(BUILD_DIR)/chess.o $(BUILD_DIR)/main.o -o $(BIN_DIR)/chess


# chess.cpp
$(BUILD_DIR)/chess.o: $(SRC_DIR)/chess.cpp
	g++ -I $(INCLUDE_DIR) -c $(SRC_DIR)/chess.cpp -o $(BUILD_DIR)/chess.o

# main.cpp
$(BUILD_DIR)/main.o: $(SRC_DIR)/main.cpp $(INCLUDE_DIR)/chess.h
	g++ -I $(INCLUDE_DIR) -c $(SRC_DIR)/main.cpp -o $(BUILD_DIR)/main.o
