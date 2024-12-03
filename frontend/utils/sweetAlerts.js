import Swal from 'sweetalert2';


 async function swalErr(falla) {
  await Swal.fire({
    icon: 'error',
    title: 'Error',
    text: falla,
  });
}

async function swalToast(icon,title) {
  const Toast = Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 2000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.onmouseenter = Swal.stopTimer;
      toast.onmouseleave = Swal.resumeTimer;
    }
  });
  Toast.fire({
    icon:icon,
    title:title
  });

}


async function swalTrue(text) {
  await Swal.fire({
    icon: 'success',
    title: 'Completado',
    text: text,
  });
}



async function swalQuestion(title, text) {
  const { isConfirmed } = await Swal.fire({
    title: title,
    text: text,
    icon: 'warning',
    showCancelButton: true,
    // confirmButtonColor:,
    cancelButtonColor: 'gray',
    confirmButtonText: 'Confirmar',
  });

  return isConfirmed;
}

async function swalconfirmation(text){
  Swal.fire(
    'Completado!',
    text,
    'success'
  );
  setTimeout( () => {document.location.reload(true)}, 1500);
}

async function swalLogin(title = "Signed in successfully", text = "") {
  Swal.mixin({
    toast: true,
    position: "top-end",
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.onmouseenter = Swal.stopTimer;
      toast.onmouseleave = Swal.resumeTimer;
    }
  });
  Toast.fire({
    icon: "success",
    title: title,
    text: text,
  });
}

async function swalInput(titulo) {
  const result = await Swal.fire({
    title: titulo,
    input: 'text',
    inputAttributes: {
      autocapitalize: 'off'
    },
    style: {
      width: '64em',
    },
    showCancelButton: true,
    confirmButtonText: 'Ingresar',
    showLoaderOnConfirm: true,
    allowOutsideClick: () => !Swal.isLoading(),
    customClass: {
      popup: 'bg-white border border-gray-300 rounded-lg shadow-lg p-6',
      title: 'text-2xl font-bold text-gray-900',
      input: 'border border-gray-300 rounded-md p-2',
      confirmButton: 'p-3 titulo  ',
      cancelButton: 'p-3 titulo'
    }
  });

  // const elemento = document.querySelector('.swal2-container');
  // elemento.style.width = '64em !important';

  return result.value;
}

export {
  swalQuestion,
  swalInput,
  swalconfirmation,
  swalErr,
  swalTrue,
  swalLogin,
  swalToast
};