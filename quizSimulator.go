package main

import ("fmt"
       // "math/rand"
       "io/ioutil"
       "strings"
       "os"
      )

func main() {
  // initialize variables
  capacity := 100
  var numOfQuestion int

  a := make([]string, capacity)

  stream, err := ioutil.ReadFile("all.txt")

  if err != nil {
    fmt.Println("Unexpected Error", err)
    os.Exit(0)
  }

  readString := string(stream)

  s := strings.Split(readString, "\n")

  fmt.Println(s)

  lineLength := len(s)

  for i := 0; i < lineLength; i++ {
    fmt.Println(string(s[i][0]))
  }

  for i := 0; i < capacity; i++ {
    if a[i] != "" {
      numOfQuestion++
    }
  }
}
