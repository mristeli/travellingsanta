(ns router.core-test
  (:require [clojure.test :refer :all]
            [router.core :refer :all]))

(def point1 (struct point 94.123 30.41))
(def north_pole (struct point 90 0))
(def south_pole (struct point -90 0))

(deftest distance-to-self
  (testing "Distance to self failed"
  (is (= 0.0 (distance point1 point1)))))
  
(deftest distance-between-poles
	(testing "Distance between poles"
	(is (= (* RADIUS Math/PI) (distance north_pole south_pole)))))