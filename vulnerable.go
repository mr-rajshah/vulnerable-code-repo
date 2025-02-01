package main

import (
    "fmt"
    "net/http"
    "os/exec"
)

func handler(w http.ResponseWriter, r *http.Request) {
    userInput := r.URL.Query().Get("cmd")
    // Command injection vulnerability
    out, _ := exec.Command("sh", "-c", userInput).Output()
    fmt.Fprintf(w, string(out))
}

func main() {
    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}
