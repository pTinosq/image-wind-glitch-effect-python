# Image wind glitch effect in Python

## Requirements
* pip install pillow

## Inputs
* `file_path` - Location of image file to affect
* `split_chance` - The probability that a pixel will result in a split (0 - 1) Higher values give more tear.
* `splitIntensity` - The amount of pixels that will slide across if a split happens. Higher values give more noticable tear.
* `splitThreshold` - The "thickness" of the tear. A higher value will give a more visible tear

## Examples
### Input image
![Input image](https://imgur.com/ISIxJz9.png "Input image")

```
Split change: 0.1
Split intensity: 50
Split threshold: 5
```
![Example #1](https://i.imgur.com/OnojG2K.png "Example #1")


```
Split change: 0.5
Split intensity: 50
Split threshold: 50
```
![Example #2](https://i.imgur.com/lJcmrMb.png "Example #2")

```
Split change: 0.01
Split intensity: 100
Split threshold: 100
```
![Example #3](https://i.imgur.com/5YCv9TE.png "Example #3")
