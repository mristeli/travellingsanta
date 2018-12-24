
(defstruct point :lat :lon)

(def squared (fn [x] (Math/pow x 2)))

(defn distance
	"Calculate the great circle distance between two points" 
	[point1 point2]
	(let [lat1 (Math/toRadians (:lat point1)) lon1 (Math/toRadians (:lon point1))
		lat2 (Math/toRadians (:lat point2)) lon2 (Math/toRadians (:lon point2))
		dlat (- lat2 lat1) dlon (- lon2 lon1) 
		a (+ (squared (Math/sin (/ dlat 2))) (* (Math/cos lat1) (Math/cos lat2) (squared (Math/sin (/ dlon 2)))))
		c (* 2 (Math/atan2 (Math/sqrt a) (Math/sqrt (- 1 a))))
		r 6378]
		(* r c)
		))
