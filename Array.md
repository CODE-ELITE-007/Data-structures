# Arrays

## Table of contents

- [Introduction](#introduction)<br>
- [Advantages and Disadvantages](#advantages-of-array)<br>
- [Arrays Java vs Cpp](#arrays-in-java-vs-cpp)<br>
- [Array vs ArrayList in java](#array-vs-arraylist-in-java)<br>
- [ArrayList methods in Java](#arrayList-methods-in-java)<br>
- [Array operations](#array-operations)
  - [Searching a element in array](#searching-a-element-in-array)
  - [Insertion and Deletion](#insertion-and-deletion)
- [LinkedList in java](#linkedlist-in-java)
- [Bibliography](#bibliography)

## Introduction

An **array** is a collection of _homogeneous_ items stored at _contigious memory locations_, which makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array).<br><br>
![array data structure](/assets/array.png)
<br>

```java
class Array {
    public static void main(String args[]) {
        char[] chararr = { 'U', 'B', 'F', 'D', 'A', 'E', 'C' };
    }
}
```

In the above example address of the first element of the array is 200. As it is a character array and each character is of size 1 byte. So that _*nth*_ element is stored at _200+(1\*(n-1))_.
<br><br>

## _Advantages of array_

- Arrays allow random access of elements. This makes accessing elements by position faster. O(1)
- Arrays have better cache locality that can make a pretty big difference in performance.

## _Disadvantages of array_

- You can’t change the size i.e. once you have declared the array you can’t change its size because of static memory allocated to it.
  **(but java Arraylists and c++ vectors are expandable)**.
- operations like deletion and insertion take significantly long time when compared to other data structures. O(n)
- push and pop operations of stack when implemented using an array have more complexity.

## Arrays in Java vs Cpp

- Arrays in c++ are allocated in a stack unless they are dynamically allocated. using the "new" operator arrays are allocated in heap.

```cpp
void main(){
  int arr[5]=[1,2,3,4,5]; // stack allocation
  int *arr=new int[5]; //heap allocation
}
```

- Arrays in java are always allocated in a heap.

```java
public static void main(String args[]){
  int[] arr=new int[5]; //heap allocation
  int arr[5]=[1,2,3,4,5]; //heap allocation
}
```

## Array vs ArrayList in java

### **Array**

- An array is a basic data structure provided by java.
- declaration :

```java
int arr[] = new int[10];
```

- array elements can be accessed using [].
- array is fixed size data structure. The size of the array neeed to be specified while initializing.
- Array can contain both primitive data types as well as objects of a class depending on the definition of the array.
- In array, it depends whether the arrays is of primitive type or object type. In case of primitive types, actual values are contiguous locations, but in case of objects, allocation is similar to ArrayList.

### **ArrayList**

- ArrayList is a part of collection frame work in java.
- declaration :

```java
import java.util.ArrayList;
ArrayList<Integer> arrL = new ArrayList<Integer>();
```

- ArrayList elements can be accessed using get() and add().
- ArrayList is expandable. Size is not necessary to be mentioned while initializing.
- ArrayList only supports object entries, not the primitive data types.
- Since ArrayList can’t be created for primitive data types, members of ArrayList are always references to objects at different memory locations (See this for details). Therefore in ArrayList, the actual objects are never stored at contiguous locations. References of the actual objects are stored at contiguous locations.
- Java ArrayList supports many additional operations like indexOf(), remove(), etc. These functions are not supported by Arrays.

## ArrayList methods in Java

> - _add(int index, E element)_ - Inserts the specified element at the specified position in this list.<br>

> - _addAll(int index, Collection<? extends E> c)_ - Inserts all of the elements in the specified collection into this list, starting at the specified position.<br>

> - _clear()_ - Removes all of the elements from this list.<br>

> - _clone()_ - Returns a shallow copy of this ArrayList instance.<br>

> - _contains(Object o)_ - Returns true if this list contains the specified element.<br>

> - _forEach(Consumer<? super E> action)_ -
>   Performs the given action for each element of the Iterable until all elements have been processed or the action throws an exception.<br>

> - _get(int index)_ -
>   Returns the element at the specified position in this list.<br>

> - _indexOf(Object o)_ -
>   Returns the index of the first occurrence of the specified element in this list, or -1 if this list does not contain the element.<br>

> - _lastIndexOf(Object o)_ -
>   Returns the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element.<br>

> - _isEmpty()_-
>   Returns true if this list contains no elements.<br>

> - _remove(int index)_ -
>   Removes the element at the specified position in this list.<br>

> - _remove(Object o)_ -
>   Removes the first occurrence of the specified element from this list, if it is present.<br>

> - _size()_ -
>   Returns the number of elements in this list.

> - _sort(Comparator<? super E> c)_ -
>   Sorts this list according to the order induced by the specified Comparator.

for other functions of ArrayList [Refer this link](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)

## Array operations

### Searching a element in array

<br>

> there are two ways to search for an element in a array :<br>
>
> - **Linear search :** linearly traversing through the array untill the key is found. if the key is found the function returns position, else -1.<br> > _Complexity : O(n)_

```java
class Search {
    public static void main(String args[]) {
        int arr[] = { 1, 2, 3, 4, 5 };
        System.out.println(linearsearch(arr, arr.length, 3));
    }

    public static int linearsearch(int arr[], int n, int x) {
        for (int i = 0; i < n; i++) {
            if (arr[i] == x) {
                return i;
            }
        }
        return -1;
    }
}
```

> - **Binary search :** Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.. if the key is found the function returns position, else -1.<br> > _Complexity : O(log n)_

```java
class Search {
    public static void main(String args[]) {
        int arr[] = { 1, 2, 3, 4, 5 };
        System.out.println(binarysearch(arr, 0, arr.length - 1, 3));
    }

    public static int binarysearch(int arr[], int l, int r, int x) {
        if (r >= l) {
            int mid = l + (r - l) / 2;
            if (arr[mid] == x)
                return mid;
            else if (arr[mid] > x)
                return binarysearch(arr, l, mid - 1, x);
            return binarysearch(arr, mid + 1, r, x);
        }
        return -1;
    }
}
```

<br>

### Insertion and Deletion

> **Insertion:** <br> > _Approach 1 :_ To insert a element in a array of length m at _nth_ position, all the elements from nth position to _(m-1)th_ position should be shifted towards right.
> _Complexity : O(n)_<br>

> _Approach 2 :_
>
> 1.  First get the element to be inserted, say element.
> 2.  Then get the position at which this element is to be inserted, say position.
> 3.  Convert array to ArrayList.
> 4.  Add element at position using list.add(position, element)
> 5.  Convert ArrayList back to array and print.
>     _Complexity : O(n)_

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
public class AddElementAtPositionInArray {
    private static void addElement( Integer[] arr, int element, int position)
    {
        List<Integer> list = new ArrayList<>(Arrays.asList(arr));
        list.add(position - 1, element);
        arr = list.toArray(arr);

        System.out.println("Initial Array:\n"+ Arrays.toString(arr));

        System.out.println("\nArray with " + element+
        " inserted at position "+ position + ":\n"+ Arrays.toString(arr));
    }
    public static void main(String[] args)
    {
        Integer[] arr = { 1, 2, 3, 4, 5,6, 7, 8, 9, 10 };

        int element = 50;
        int position = 5;
        addElement(arr, element, position);
    }
}
```

## LinkedList in java

The LinkedList stores its items in "containers." The list has a link to the first container and each container has a link to the next container in the list. To add an element to the list, the element is placed into a new container and that container is linked to one of the other containers in the list.

```java
import java.util.LinkedList;

public class MyClass {
  public static void main(String[] args) {
    LinkedList<String> cars = new LinkedList<String>();
    cars.add("Volvo");
    cars.add("BMW");
    cars.add("Ford");
    cars.add("Mazda");
    System.out.println(cars);
  }
}
```

_Note: LinkedList methods are same as that of ArrayList._

## Bibliography

[Oracle](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html)<br>
[Geeksforgeeks](https://www.geeksforgeeks.org/array-data-structure/)<br>
[w3schools](https://www.w3schools.com/java/java_arraylist.asp)
