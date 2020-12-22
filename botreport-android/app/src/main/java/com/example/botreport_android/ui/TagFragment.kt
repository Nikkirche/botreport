package com.example.botreport_android.ui

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.commit
import androidx.lifecycle.lifecycleScope
import com.example.botreport_android.R
import com.example.botreport_android.databinding.ArticleFeedFragmentBinding.inflate
import com.example.botreport_android.databinding.FragmentTagBinding
import com.example.botreport_android.databinding.LiveNewsFeedFragmentBinding
import com.example.botreport_android.databinding.MainActivityBinding.inflate
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import moxy.MvpAppCompatFragment
import reactivecircus.flowbinding.android.view.clicks

@AndroidEntryPoint
class TagFragment : MvpAppCompatFragment() {
    private var _binding: FragmentTagBinding? = null
    private val binding get() = _binding!!
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = FragmentTagBinding.inflate(inflater, container, false)
        val view = binding.root
        binding.backFromTag.clicks().onEach {
            parentFragmentManager.popBackStack()
        }.launchIn(viewLifecycleOwner.lifecycleScope)
        return  view
    }


}