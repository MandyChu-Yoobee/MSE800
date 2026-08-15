# Week 2 - Activity 1.2: Optimization - BMI calculator project

Optimize the code below and try to remove the use of `this` where possible (explain why or why not). The goal of this activity is to better understand how `this` works and when it is needed. Share your optimized code by posting the GitHub link here. See help link: [GitHub - eduards-lv/Activity_1-4: Week 1 Activity 4 · GitHub](https://github.com/eduards-lv/Activity_1-4)

## Reference code (before)

```python
def isfloat(n):
  """
  If string can be converted to floating number
  returns that number, otherwise returns false
  """
  try:
    n=float(n)
    return n;
  except ValueError:
     return False;

def inputfloat(hint):
  """
  Prints hint and asks to enter number.
  Repeats until decimal number is entered.
  """
  ret = False
  while ret is False:
    ret = isfloat(input(hint))
    if ret is False:
      print("Please enter number")
  return ret

class BMIcalculator:
  def getdata(this):
    """
    Get weight in kgs and height in cms.
    Height is entered in cetimetres and stored in metres
    """

    this.w = inputfloat("Please enter your weight in kilograms:")
    this.h = inputfloat("Please enter your height in centimetres:")/100

  def calculate(this):
    """
    Calculate and return bmi
    """

    return round(this.w/(this.h*this.h),2)


def main():
  print("\n","="*42,"\n")
  print("Hello, let's calculate your BMI.");

  calc = BMIcalculator()
  print()
  calc.getdata()
  bmi=calc.calculate()
  print(f"Your BMI is {bmi}")
  print("\n","="*42,"\n")

if __name__ == "__main__":
    main()
```

## What `this` is (in this code)

The reference code names its methods' first parameter `this`, which is JavaScript
terminology. In Python the equivalent reference is written as `self` — it is not
a keyword, just a strong convention. It is the reference to the *specific object*
a method was called on, and it is the only way a method can reach that object's
own attributes.

## Where `this`/`self` can be removed (and why)

- **`isfloat` / `inputfloat`** never touch `self` at all — they are standalone
  helper functions. They are already correctly written *without* a `self`
  parameter, and in the optimized version they stay self-contained. No removal
  was needed here because they never used `self` in the first place.

## Where `this`/`self` cannot be removed (and why)

- **`getdata`** stores the user's weight and height on the object
  (`self.weight_kg`, `self.height_m`). Storing *per-object state* requires `self`.
- **`calculate`** reads that stored state back. `self` is needed because it is
  how the two methods communicate — `getdata` writes the values, `calculate`
  reads them.

The only way to remove `self` from these two methods entirely would be to stop
using an object: make `getdata` *return* `(weight, height)` and make `calculate`
*take* `(weight, height)` as arguments. That works, but it turns the class into a
plain collection of functions with no state — which defeats the point of OOP.

## Conclusion

`this`/`self` is needed whenever a method must read or write data that belongs to
a specific object, and especially when two methods need to share that data. It can
be omitted only for methods that are pure/stateless — ones that work solely on
their arguments (like `isfloat` and `inputfloat`).
