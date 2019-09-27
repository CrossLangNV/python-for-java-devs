package com.crosslang.courses;

public class BiGram implements NGram {

	private String text;
	
	public BiGram(String text) {
		this.text = text;
	}
	
	@Override
	public int getOrder() {
		return 2;
	}

	@Override
	public String getText() {
		return this.text;
	}
	
	@Override
	public String toString() {
		return "bigram" + this.text ;
	}
}
