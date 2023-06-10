package isomorphic_strings

func isIsomorphic(s string, t string) bool {
	rep := make(map[byte]byte)
	usd := make(map[byte]bool)
	for i := 0; i < len(s); i++ {
		si := s[i]
		ti := t[i]
		if val, ok := rep[si]; ok {
			if val != ti {
				return false
			}
		} else {
			if _, ok := usd[ti]; ok {
				return false
			}
			rep[si] = ti
			usd[ti] = true
		}
	}
	return true
}
