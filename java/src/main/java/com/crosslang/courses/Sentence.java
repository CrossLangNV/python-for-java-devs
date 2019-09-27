package com.crosslang.courses;

import java.util.ArrayList;
import java.util.List;

public class Sentence {
	
	private List<NGram> nGrams;
	
	public Sentence() {
		nGrams = new ArrayList<NGram>();
	}
	
	public void addNgram(NGram ngram) {
		nGrams.add(ngram);
	}
	
	public List<NGram> getNGrams() {
		return this.nGrams;
	}

}
