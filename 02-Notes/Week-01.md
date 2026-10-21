# Week 1 Notes

## What I Learned

Python is object-oriented.

## Questions

- What is __repr__()?
- What is __len__()?

## Explaining FrenchDeck Code
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

 ## Explaining collections.nameturple
 Card = collections.namedtuple('Card', ['rank', 'suit'])
## the stament/line creates a brand-new class called Card.
## It is same as writing 
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
## A class is like a blueprint or template. 
class Card: 
## The above means that I am creating a blueprint called class

class Card:
    def __init__(self, rank, suit):

## Considering the statement/line above,The __init__ method is called the constructor. 
## It runs automatically every time you create a new object.Think of it as the setup method.
## Whenever Python creates a new Card, it asks: "What values should this new card have?"
## Answer is rank and suits
## self means "This particular object."
## self.rank = rank , Store the value of rank inside this object.
## self.suit = suit, Store the value of suit inside this object.
## The key idea to remember

When you write:

card = Card("A", "spades")

you're telling Python:

Create a new Card object.
Run the __init__ method automatically.
Store "A" in self.rank.
Store "spades" in self.suit.
Assign the newly created object to the variable card.

If you're learning Fluent Python, this concept is essential because almost every example in the book builds on understanding classes, objects, attributes, and the special role of self.

# The code below, is called  a nested list comprehension and is exactly same as the one that follows
self._cards = [
    Card(rank, suit)
    for suit in self.suits
    for rank in self.ranks
]

## This code is exactly same as above 
self._cards = []

for suit in self.suits:
    for rank in self.ranks:
        self._cards.append(Card(rank, suit))

## what does this self._cards mean?
## What is self?

You already know that self refers to the current object.
Suppose we create a deck:
## deck = FrenchDeck()

Python creates one object in memory.
We can imagine it like this:

deck
 │
 ▼
+--------------------+
| FrenchDeck Object  |
|                    |
|                    |
+--------------------+
Inside the class, whenever Python says
self it means

"This FrenchDeck object."

## What exactly is stored inside _cards?

This line

self._cards = [
    Card(rank, suit)
    for suit in self.suits
    for rank in self.ranks
]

creates a list.

That means _cards is just a normal Python list.

Imagine it like this:

_cards

[
    Card("2","spades"),
    Card("3","spades"),
    Card("4","spades"),
    ...
    Card("A","hearts")
]

It is no different from writing

numbers = [10,20,30]

except instead of numbers, the list contains Card objects.

## Visualize the object

Suppose we write

deck = FrenchDeck()

After the constructor finishes, memory looks like this:

deck
 │
 ▼
+------------------------------------+
| FrenchDeck Object                  |
|                                    |
| _cards ------------------------+   |
+--------------------------------|---+
                                 |
                                 ▼
        +-----------------------------------------+
        | List                                    |
        |                                         |
        | [0] Card("2","spades")                  |
        | [1] Card("3","spades")                  |
        | [2] Card("4","spades")                  |
        | [3] Card("5","spades")                  |
        | ...                                     |
        | [51] Card("A","hearts")                 |
        +-----------------------------------------+

Notice something important:

The FrenchDeck object doesn't directly contain the cards.

Instead, it contains one attribute called _cards, and _cards is a list containing all 52 cards.

## Think of a bookshelf

Imagine your deck is actually a bookshelf.

Bookshelf

Inside the bookshelf is a shelf called

books
Bookshelf

books
 ├── Book 1
 ├── Book 2
 ├── Book 3
 ├── ...
 └── Book 52

In the code,

books

is exactly like

_cards

The FrenchDeck object owns the shelf, and the shelf holds all the cards.

## When you see

self._cards

don't think of it as something mysterious.

Read it as:

"The list of cards that belongs to this particular deck."

So this line:

self._cards = [...]

simply means:

"Create a list containing all 52 Card objects, and store that list inside this FrenchDeck object under the attribute named _cards."

## Imagine a Car

Suppose you own a car.

The car has:

A color
A model
An engine
Four tyres

We can represent this in Python like this:

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

Now let's define the terms.

## 1. What is a Class?

A class is a blueprint.

class Car:

This is not a car.

It is only the design for making cars.

Think of it like this:

Blueprint
   │
   ▼
+----------------+
|     Car        |
|                |
| Color          |
| Model          |
+----------------+

No real car exists yet.

##  2. What is an Object?

Now we create a car.

my_car = Car("Red", "Toyota")

This is an object.

Think of it like this:

Blueprint
     │
     ▼
Car Class
     │
     ▼
my_car

Now a real car exists.

## 3. What is an Attribute?

Every object has information stored inside it.

For our car:

my_car

Color = Red
Model = Toyota

The Color and Model are called attributes.

They belong to the object.

Here's the relationship
Class
   │
creates
   ▼
Object
   │
contains
   ▼
Attributes

This relationship is very important.

Now let's return to your example.
The Class
class FrenchDeck:

This is only the blueprint.

No deck exists yet.

The Object

When we write

deck = FrenchDeck()

Python creates an object.

deck

is an object.

Think of it like this:

FrenchDeck Class
        │
creates │
        ▼
deck
The Attributes

Inside the object are variables.

One of them is

self._cards

So after creation, the object looks like this:

deck
│
▼

FrenchDeck Object

_cards = [52 Card objects]

Notice carefully:

deck is the object.
_cards is an attribute of the object.
Where do the Card objects come in?

This is another place where beginners get confused.

Remember this line?

Card(rank, suit)

Every time Python executes it, it creates another object.

For example,

Card("A", "spades")

creates

Card Object

rank = A
suit = spades

Notice something.

This is another object, not the deck.

## When Python creates all 52 cards, _cards becomes

_cards

[
   Card Object,
   Card Object,
   Card Object,
   ...
   Card Object
]

So:

_cards is one attribute.
The value of that attribute is a list.
That list contains 52 Card objects.
Let's draw everything together.
FrenchDeck Class
        │
        │ creates
        ▼
+--------------------------------+
| deck (FrenchDeck Object)       |
|                                |
| _cards ---------------------+  |  ← Attribute
+-----------------------------|--+
                              |
                              ▼
                    List (Attribute Value)

                    +--------------------+
                    | Card Object        |
                    | rank = 2           |
                    | suit = spades      |
                    +--------------------+

                    +--------------------+
                    | Card Object        |
                    | rank = 3           |
                    | suit = spades      |
                    +--------------------+

                    ...

                    +--------------------+
                    | Card Object        |
                    | rank = A           |
                    | suit = hearts      |
                    +--------------------+
Think of a School

Imagine a school.

School

Inside the school is a classroom.

Classroom

Inside the classroom are students.

Student 1
Student 2
Student 3

In Python terms:

School Object

contains

classroom

which is an attribute.

The classroom contains

Student Objects

Notice that:

The classroom is not a student.
The classroom is an attribute that holds students.

Likewise:

_cards is not a Card object.
_cards is an attribute whose value is a list of Card objects.
A table that summarizes everything
Thing	In the FrenchDeck example	What it is
FrenchDeck	class FrenchDeck:	Class (blueprint)
deck	deck = FrenchDeck()	Object
_cards	self._cards	Attribute of deck
[ ... ]	Value stored in _cards	List
Card("A", "spades")	One playing card	Card object
rank	"A"	Attribute of a Card object
suit	"spades"	Attribute of a Card object
The key insight

There are different kinds of objects in this example:

A FrenchDeck object (deck)
A list object (_cards holds this list)
Fifty-two Card objects (inside the list)

So when I called _cards an attribute, I was referring to its role inside the FrenchDeck object.

When I talked about Card objects, I was referring to the 52 separate objects stored inside that attribute.

These are different things:

deck → an object.
deck._cards → an attribute of deck.
The value of deck._cards → a list object.
Each element in that list → a Card object.

I think I can make this even clearer by drawing the actual memory diagram of what Python creates after executing:

deck = FrenchDeck()

showing the FrenchDeck object, the _cards attribute, the list object, and the first few Card objects connected by arrows. That visual usually makes everything click.

## A container sequence holds references to the objects it contains, which may be of any
type, while a flat sequence stores the value of its contents in its own memory space,not as distinct Python objects

## Mutable vs Immutable Sequences

Before we define them, let's first answer:

## What is a sequence?

A sequence is a collection of items arranged in a specific order.

Examples:

"Hello" → sequence of characters
[1, 2, 3] → sequence of integers
(10, 20, 30) → sequence of integers

The order matters.

## Mutable Sequence

A mutable sequence is a sequence whose contents can be changed after it has been created.

Think of a whiteboard.

You can

erase
add
modify
rearrange

anything written on it.

Python examples:

list
bytearray
array.array
deque

## Immutable Sequence

An immutable sequence cannot be changed after it is created.

Think of a printed book.

Once it's printed,

you can't erase a page,
you can't insert another page,
you can't rewrite page 5.

If you want changes, you create another edition of the book.

Python examples:

tuple
str
bytes

## Part 2: Flat Sequence vs Container Sequence

This distinction is different.

It is not about changing data.

It is about how data is stored.

## Flat Sequence

## A flat sequence stores the actual values themselves.

Think  Egg tray

Another example

from array import array

numbers = array('i', [10,20,30])

Memory

10

20

30

## Container Sequence

## A container sequence stores references to objects, not necessarily the objects' raw values.

Think of a filing cabinet.
Each drawer doesn't contain the person—it contains a file pointing to the person's information.
Examples

list
tuple
collections.deque
Example
student = ["Taiwo", 30, True]

Memory looks conceptually like this:

student

│

├──► "Taiwo"

├──► 30

└──► True

The list stores references to objects.

Real-life analogy

Imagine a parking lot.

## Flat sequence

Each parking space contains

🚗
🚗
🚗

The cars themselves.

## Container sequence

Each parking space contains

Ticket #101

Ticket #205

Ticket #998

The ticket tells you where the car is.

Lists and tuples behave more like this conceptually—they can contain references to many different kinds of objects.

## What is a List?

A list is simply a container that stores items in order.

For example:

fruits = ["Apple", "Orange", "Banana"]

fruits

+---------+
| Apple   |
| Orange  |
| Banana  |
+---------+

hat is a List Comprehension?

A list comprehension is a short and elegant way of creating a list.

Instead of writing many lines of code with a loop, Python allows us to create a list in one expression.

Example 1

Suppose you want a list containing the numbers 1 to 5.

Method 1 — Using a loop
numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

Output

[1, 2, 3, 4, 5]
Method 2 — Using a list comprehension
numbers = [i for i in range(1, 6)]

print(numbers)

Output

[1, 2, 3, 4, 5]

Exactly the same result.

The second version is just much shorter.