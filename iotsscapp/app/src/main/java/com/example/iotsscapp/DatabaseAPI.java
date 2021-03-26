package com.example.iotsscapp;

import java.util.List;
import retrofit2.Call;
import retrofit2.http.GET;

public interface DatabaseAPI {

    @GET("history")
    Call<List<Sample>> getSamples();

}