# photomosaic

This application allows you to upload a library of random images that can be used to create a photomosaic of an input image. There is both a “simple” and “advanced” option for the application.

## Requirements

Python 2.x, numpy, cv2, pandas

## How to Run

* Clone this repo
* Create an `images` directory and add as many images to it as you desire (recommend no less than 300)
* Run python `create_image_index.py images`
* To run the simple algorithm, run `python create_photomosaic.py [input image] [tile_size] simple `
* To run the advanced algorithm, run `python create_photomosaic.py [input image] [tile_size] advanced images `
* Any time you update your library, rerun `create_image_index.py images`

## Examples

### Simple Algorithm

#### Flower Image Original 
![Alt text](/input_output/flowers.jpg?raw=true "Original Image")

##### 50 x 50 Tile Replacement
![Alt text](/input_output/simple_mosaic_50flowers.jpg?raw=true "50 x 50 Tile Replacement")

##### 20 x 20 Tile Replacement
![Alt text](/input_output/simple_mosaic_20_flowers.jpg?raw=true "20 x 20 Tile Replacement")

##### 10 x 10 Tile Replacement
![Alt text](/input_output/simple_mosaic_10flowers.jpg?raw=true "10 x 10 Tile Replacement")

##### 5 x 5 Tile Replacement
![Alt text](/input_output/simple_mosaic_5flowers.jpg?raw=true "5 x 5 Tile Replacement")

### Complex Algorithm

#### Flower Image Original 
![Alt text](/input_output/flowers.jpg?raw=true "Original Image")

##### 50 x 50 Tile Replacement
![Alt text](/input_output/advanced_mosaic_50flowers.jpg?raw=true "50 x 50 Tile Replacement")

##### 20 x 20 Tile Replacement
![Alt text](/input_output/advanced_mosaic_20flowers.jpg?raw=true "20 x 20 Tile Replacement")

##### 10 x 10 Tile Replacement
![Alt text](/input_output/advanced_mosaic_10flowers.jpg?raw=true "10 x 10 Tile Replacement")

##### 5 x 5 Tile Replacement
![Alt text](/input_output/advanced_mosaic_5flowers.jpg?raw=true "5 x 5 Tile Replacement")

