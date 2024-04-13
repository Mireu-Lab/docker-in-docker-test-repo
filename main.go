package main

import (
	"time"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.LoadHTMLGlob("web/*")

	router.GET("/", func(c *gin.Context) {
		c.JSONP(200, gin.H{"msg": "pong", "time": time.RFC3339})
	})
	router.Run(":80")
}
