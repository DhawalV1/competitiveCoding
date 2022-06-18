class Solution:
	def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
		
		def distance(point1, point2):
			return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
		
		def are_diagonals_middle_point_the_same(po1, po2, po3, po4):
			return po1[0] + po2[0] == po3[0] + po4[0] and po1[1] + po2[1] == po3[1] + po4[1]
		
		def are_diagonals_have_equal_length(po1, po2, po3, po4):
			return distance(po1, po2) == distance(po3, po4) and distance(po1, po4) == distance(po2, po4)
		
		def are_points_are_merge(po1, po2, po3, po4):
			return po1 != po2
		
		def check_square(po1, po2, po3, po4):
				return are_diagonals_middle_point_the_same(po1, po2, po3, po4) and are_diagonals_have_equal_length(po1, po2, po3, po4) and are_points_are_merge(po1, po2, po3, po4)
					
		return check_square(p1, p2, p3, p4) or check_square(p1, p3, p2, p4) or check_square(p1, p4, p2, p3)
	