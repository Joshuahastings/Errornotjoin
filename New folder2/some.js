const numbers = [1,2,3,4,5,6,7,8,9,10]
var test_man = 0 
var test_dog = 1
var test_cat = 0

//add them all up
test_man = numbers[0] + numbers [1]
test_dog = test_man + numbers[2]
test_cat = test_dog + numbers[3]
test_man = test_cat + numbers[4]
test_dog = test_man + numbers[5]
test_cat = test_dog + numbers[6]
test_man = test_cat + numbers[7]
test_dog = test_man + numbers[8]
test_cat = test_dog + numbers[9]
console.log(test_cat)
//add then div
var dogs_and_cats  = [20, 30, 25, 35, -16, 60, -100]
var dogs = 0
var cats = 0 
dogs = dogs_and_cats[0] + dogs_and_cats [1]
cats = dogs + dogs_and_cats[2]
dogs = cats + dogs_and_cats[3]
cats = dogs + dogs_and_cats[4]
dogs = cats + dogs_and_cats[5]
cats = dogs + dogs_and_cats[6]
dogs = cats / dogs_and_cats.length
console.log(dogs);
//max and min
const dogs_that_can_fly = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
var dogs_that = Math.max(25, 14, 56, 15, 36, 56, 77, 18, 29, 49)
var cats_that = Math.min(25, 14, 56, 15, 36, 56, 77, 18, 29, 49)
console.log(dogs_that)
console.log(cats_that)