(ns router.core
  (:gen-class))



(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))

(defstruct point :lat :lon)
(def RADIUS 6378)

(def squared (fn [x] (Math/pow x 2)))

(defn distance
	"Calculates the great circle distance between two points (struct point)" 
	[point1 point2]
	(let [lat1 (Math/toRadians (:lat point1)) lon1 (Math/toRadians (:lon point1))
  		lat2 (Math/toRadians (:lat point2)) lon2 (Math/toRadians (:lon point2))
  		dlat (- lat2 lat1) dlon (- lon2 lon1) 
  		a (+ (squared (Math/sin (/ dlat 2))) (* (Math/cos lat1) (Math/cos lat2) (squared (Math/sin (/ dlon 2)))))
  		c (* 2 (Math/atan2 (Math/sqrt a) (Math/sqrt (- 1 a))))
  		]
  		(* RADIUS c)
  		))
