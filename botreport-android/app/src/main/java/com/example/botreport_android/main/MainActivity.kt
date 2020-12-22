package com.example.botreport_android.main
import android.os.Bundle
import com.example.botreport_android.R
import com.example.botreport_android.presenter.MainPresenter
import com.example.botreport_android.presenter.NewsFlowPresenter
import com.example.botreport_android.views.MainView
import dagger.hilt.android.AndroidEntryPoint
import moxy.MvpAppCompatActivity
import moxy.ktx.moxyPresenter
import moxy.presenter.InjectPresenter
import moxy.presenter.ProvidePresenter
import javax.inject.Inject
import javax.inject.Provider


@AndroidEntryPoint
class MainActivity : MvpAppCompatActivity(),MainView{
    @Inject
    lateinit var presenterProvider: Provider<MainPresenter>
    private val presenter: MainPresenter by moxyPresenter { presenterProvider.get() }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.main_activity)

    }
}
