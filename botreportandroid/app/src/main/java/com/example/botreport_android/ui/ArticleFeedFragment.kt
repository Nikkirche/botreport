package com.example.botreport_android.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import com.example.botreport_android.databinding.ArticleFeedFragmentBinding
import com.example.botreport_android.databinding.LiveNewsFeedFragmentBinding
import moxy.MvpAppCompatFragment

class ArticleFeedFragment:MvpAppCompatFragment() {
    private var _binding: ArticleFeedFragmentBinding? = null
    private val binding get() = _binding!!
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        _binding = ArticleFeedFragmentBinding.inflate(inflater, container, false)
        val view = binding.root
        return view
    }
}